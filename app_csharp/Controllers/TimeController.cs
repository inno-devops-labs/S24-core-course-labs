using Domain.Services;
using Microsoft.AspNetCore.Mvc;

namespace Controllers;

/// <summary>
/// Operations with time
/// </summary>
[ApiController]
[Route("time")]
public class TimeController(IDateTimeProvider dateTimeProvider) : Controller
{
    /// <summary>
    /// Get current time in MSK timezone
    /// </summary>
    [Route("msk")]
    [HttpGet]
    public CurrentTimeResponse GetTimeInMsk()
    {
        return new CurrentTimeResponse(dateTimeProvider.NowMsk());
    }
}