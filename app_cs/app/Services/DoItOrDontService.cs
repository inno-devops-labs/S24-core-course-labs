using Microsoft.AspNetCore.Mvc;

namespace app_cs.App.Services;

public interface IDoItOrDontService
{
    public string GetOption();
}

public class DoItOrDontService : IDoItOrDontService
{
    private static readonly string[] Options = ["Do it", "Do not do it"];

    public string GetOption()
    {
        return Options[new Random().Next(0, Options.Length)];
    }
}