using System.Text.Json.Serialization;

namespace app_dotnet.Services;

public interface IDoItOrDontService
{
    public Option GetOption();
}

public class Option
{
    public Option(string yourOption)
    {
        YourOption = yourOption;
    }

    [JsonPropertyName("your_option")]
    public string YourOption { get; set; }
}

public class DoItOrDontService : IDoItOrDontService
{
    private static readonly string[] Options = {"Do it", "Do not do it"};

    public Option GetOption()
    {
        return new Option(Options[new Random().Next(0, Options.Length)]);
    }
}