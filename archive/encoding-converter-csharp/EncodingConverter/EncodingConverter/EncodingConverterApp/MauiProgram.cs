using Microsoft.Extensions.Logging;
using Microsoft.Maui.LifecycleEvents;

namespace EncodingConverterApp
{
    public static class MauiProgram
    {
        public static MauiApp CreateMauiApp()
        {
            var builder = MauiApp.CreateBuilder();
            builder
                .UseMauiApp<App>()
                .ConfigureFonts(fonts =>
                {
                    fonts.AddFont("OpenSans-Regular.ttf", "OpenSansRegular");
                    fonts.AddFont("OpenSans-Semibold.ttf", "OpenSansSemibold");
                })
                .ConfigureLifecycleEvents(events =>
                 {
#if WINDOWS
                     events.AddWindows(wnd =>
                     {
                         wnd.OnWindowCreated(window =>
                         {
                             var hwnd = WinRT.Interop.WindowNative.GetWindowHandle(window);
                             var windowId = Microsoft.UI.Win32Interop.GetWindowIdFromWindow(hwnd);
                             var appWindow = Microsoft.UI.Windowing.AppWindow.GetFromWindowId(windowId);

                             // Устанавливаем размер окна
                             var preferredSize = new Windows.Graphics.SizeInt32(1280, 720);
                             appWindow.Resize(preferredSize);

                             // Запрещаем изменение размера окна
                             appWindow.SetPresenter(Microsoft.UI.Windowing.AppWindowPresenterKind.Default);
                             var presenter = (Microsoft.UI.Windowing.OverlappedPresenter)appWindow.Presenter;
                             presenter.IsResizable = false;
                             presenter.IsMaximizable = false;

                             // Центрируем окно на экране
                             var displayArea = Microsoft.UI.Windowing.DisplayArea.GetFromWindowId(windowId, Microsoft.UI.Windowing.DisplayAreaFallback.Primary);
                             var centerPosition = new Windows.Graphics.PointInt32(
                                 (displayArea.WorkArea.Width - preferredSize.Width) / 2,
                                 (displayArea.WorkArea.Height - preferredSize.Height) / 2
                             );
                             appWindow.Move(centerPosition);
                         });
                     });
#endif
                 });

#if DEBUG
            builder.Logging.AddDebug();
#endif

            return builder.Build();
        }
    }
}
