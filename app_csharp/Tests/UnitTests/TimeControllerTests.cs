using Controllers;
using Domain.Services;
using NSubstitute;

namespace UnitTests;

public class TimeControllerTests
{
    [Fact]
    public void TimeController_Should_ReturnInExpectedFormat()
    {
        // Arrange
        var mockService = Substitute.For<IDateTimeProvider>();
        var constDateTime = DateTimeOffset.Parse("2024-02-19T22:19:11.112401+03:00");
        mockService.NowMsk().Returns(constDateTime);
        var controller = new TimeController(mockService);
        
        // Act
        var returnedTimeInfo = controller.GetTimeInMsk();
        
        // Assert
        Assert.Equivalent(
            returnedTimeInfo,
            new CurrentTimeResponse(constDateTime));
    }
}