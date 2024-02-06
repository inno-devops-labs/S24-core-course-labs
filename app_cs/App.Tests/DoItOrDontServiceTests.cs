using Xunit;
using App.Controllers;
using app_cs.App.Services;

namespace Prime.UnitTests.Services;

public class DoItOrDont_ValidRequest_ShouldReturn200OK
{
    private readonly DoItOrDontService _target = new();

    [Fact]
    public void GetOption_ValidGet_ReturnsOneOfTwoOptions()
    {
        var response = _target.GetOption();
        Assert.True(response == "Do it" || response == "Do not do it");
    }
}
