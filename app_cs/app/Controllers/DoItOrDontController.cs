using app_cs.App.Services;
using Microsoft.AspNetCore.Mvc;

namespace App.Controllers;

[ApiController]
[Route("/")]
public class DoItOrDontContoller : ControllerBase
{
    private readonly ILogger<DoItOrDontContoller> _logger;
    private readonly IDoItOrDontService _doItOrDontService;

    public DoItOrDontContoller(ILogger<DoItOrDontContoller> logger, IDoItOrDontService doItOrDontService)
    {
        _logger = logger;
        _doItOrDontService = doItOrDontService;
    }

    [HttpGet]
    public string Get()
    {
        return _doItOrDontService.GetOption();
    }
}
