namespace EncodingConverterApp
{
    public partial class MainPage : ContentPage
    {
        private string? sourceFilePath;
        private string? targetEncoding;

        public MainPage()
        {
            InitializeComponent();
        }

        private async void OnSelectFileClicked(object sender, EventArgs e)
        {
            try
            {
                var filePicker = await Microsoft.Maui.Storage.FilePicker.Default.PickAsync(new PickOptions
                {
                    PickerTitle = "Выберите файл"
                });

                if (filePicker != null)
                {
                    sourceFilePath = filePicker.FullPath;
                    filePathLabel.Text = $"Выбран файл: {filePicker.FileName}";
                }

                convertButton.IsEnabled = !string.IsNullOrEmpty(targetEncoding) && !string.IsNullOrEmpty(sourceFilePath);
            }
            catch (Exception ex)
            {
                await DisplayAlert("Ошибка", "Не удалось выбрать файл: " + ex.Message, "ОК");
            }
        }

        private void OnTargetEncodingPickerSelectedIndexChanged(object sender, EventArgs e)
        {
            var picker = sender as Picker;

            if (picker?.SelectedItem != null)
            {
                targetEncoding = picker.SelectedItem.ToString();
                convertButton.IsEnabled = !string.IsNullOrEmpty(targetEncoding) && !string.IsNullOrEmpty(sourceFilePath);
            }
        }

        private void OnConvertButtonClicked(object sender, EventArgs e)
        {
            try
            {
               
            }
            catch (Exception ex)
            {

                throw;
            }
        }
    }
}
