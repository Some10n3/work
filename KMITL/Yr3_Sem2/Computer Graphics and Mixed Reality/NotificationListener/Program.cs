using System;
using System.Diagnostics.Eventing.Reader;

class Program
{
    static void Main()
    {
        Console.WriteLine("Starting event log watcher...");

        string query = "*[System[(EventID=3049)]]"; // Change if needed
        // EventLogQuery eventQuery = new EventLogQuery("Microsoft-Windows-PushNotifications-Platform/Operational", PathType.LogName, query);
        EventLogQuery eventQuery = new EventLogQuery("Application", PathType.LogName, "*[System[(Level=2)]]");

        EventLogWatcher watcher = new EventLogWatcher(eventQuery);

        watcher.EventRecordWritten += (sender, e) =>
        {
            Console.WriteLine("Event detected!");
            if (e.EventRecord != null)
            {
                Console.WriteLine($"Notification Received: {e.EventRecord.FormatDescription()}");
            }
            else
            {
                Console.WriteLine("Received an event, but no record details.");
            }
        };

        watcher.Enabled = true;
        Console.WriteLine("Watcher enabled: " + watcher.Enabled);

        Console.WriteLine("Listening for notifications...");
        Console.ReadLine();
    }
}
