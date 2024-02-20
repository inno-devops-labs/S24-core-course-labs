using System.Text.Json;
using System.Text.Json.Serialization;
using app_dotnet.Services;
using Microsoft.AspNetCore.Mvc;

namespace app_dotnet.Controllers;

[ApiController]
[Route("/")]
public class DoItOrDontController : ControllerBase
{
    private readonly ILogger<DoItOrDontController> _logger;
    private readonly IDoItOrDontService _doItOrDontService;

    public DoItOrDontController(ILogger<DoItOrDontController> logger, IDoItOrDontService doItOrDontService)
    {
        _logger = logger;
        _doItOrDontService = doItOrDontService;
    }

    [HttpGet]
    public IActionResult Get()
    {
        _logger.LogInformation("returned option");
        var ret = _doItOrDontService.GetOption();
        var json = JsonSerializer.Serialize(ret);
        return Ok(json);
    }
}