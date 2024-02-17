using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace MoscowTime.Pages;

public class IndexModel : PageModel
{
    private readonly ILogger<IndexModel> _logger;
    public string? CurrentTime { get; private set; }

    public IndexModel(ILogger<IndexModel> logger)
    {
        _logger = logger;
    }

    public void OnGet()
    {
        var timeZone = TimeZoneInfo.FindSystemTimeZoneById("Europe/Moscow");
        CurrentTime = TimeZoneInfo
            .ConvertTime(DateTime.Now, timeZone)
            .ToString("HH:mm:ss");
    }
}