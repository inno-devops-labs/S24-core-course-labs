using Xunit;
using app_dotnet.Services;

namespace Prime.UnitTests.Services;

public class DoItOrDont_ValidRequest_ShouldReturn200OK
{
    private readonly DoItOrDontService _target = new();

    [Fact]
    public void GetOption_ValidGet_ReturnsOneOfTwoOptions()
    {
        var response = _target.GetOption();
        
        Assert.True(response.YourOption is "Do it" or "Do not do it");
    }
}