
using System.Security.Cryptography;

namespace FileSignatureApp
{
    public partial class MainPage : ContentPage
    {
        private string? filePath;

        public MainPage()
        {
            InitializeComponent();
        }

        private async void OnPickFileClicked(object sender, EventArgs e)
        {
            try
            {
                var filePicker = await Microsoft.Maui.Storage.FilePicker.Default.PickAsync(new PickOptions
                {
                    PickerTitle = "Выберите файл для подписи"
                });

                if (filePicker != null)
                {
                    filePath = filePicker.FullPath;
                    filePathLabel.Text = $"Выбран файл: {filePicker.FileName}";
                    createSignatureButton.IsEnabled = true;
                }
            }
            catch (Exception ex)
            {
                await DisplayAlert("Ошибка", "Не удалось выбрать файл: " + ex.Message, "OK");
            }
        }

        private string GenerateMD5Signature(byte[] fileData)
        {
            using (System.Security.Cryptography.MD5 md5 = System.Security.Cryptography.MD5.Create())
            {
                byte[] hash = md5.ComputeHash(fileData);
                return System.BitConverter.ToString(hash).Replace("-", "").ToLower();
            }
        }

        private async void OnCreateSignatureClicked(object sender, EventArgs e)
        {
            try
            {
                byte[] fileData = File.ReadAllBytes(filePath);
                string signature = GenerateMD5Signature(fileData);
                using (Aes aes = Aes.Create())
                {
                    aes.GenerateKey();
                    aes.GenerateIV();

                    ICryptoTransform encryptor = aes.CreateEncryptor(aes.Key, aes.IV);

                    using (MemoryStream ms = new MemoryStream())
                    {
                        using (CryptoStream cs = new CryptoStream(ms, encryptor, CryptoStreamMode.Write))
                        {
                            using (StreamWriter sw = new StreamWriter(cs))
                            {
                                sw.Write(signature);
                            }
                        }
                        signature = Convert.ToBase64String(ms.ToArray());
                    }
                    signatureLabel.Text = $"ЭЦП: {signature}";
                }
            }
            catch (Exception ex)
            {
                await DisplayAlert("Ошибка", "Не удалось создать подпись: " + ex.Message, "OK");
            }
        }
    }
}
