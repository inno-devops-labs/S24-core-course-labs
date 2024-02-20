using Implementation.Services;

namespace UnitTests;

public class TimeServiceTests
{
    [Fact]
    public void TimeServiceGet_Should_BeInMsk()
    {
        // Arrange
        var mskTimezone = TimeZoneInfo.FindSystemTimeZoneById("Europe/Moscow");
        var service = new DateTimeProvider();
        
        // Act
        var preCallTime = TimeZoneInfo.ConvertTime(DateTimeOffset.Now, mskTimezone);
        var serviceTime = service.NowMsk();
        var postCallTime = TimeZoneInfo.ConvertTime(DateTimeOffset.Now, mskTimezone);
        
        // Assert
        Assert.True(serviceTime > preCallTime);
        Assert.True(serviceTime < postCallTime);
    }
    
    [Fact]
    public void TimeServiceGet_Should_ChangeWithTime()
    {
        // Arrange
        var service = new DateTimeProvider();
        
        // Act
        var serviceTime1 = service.NowMsk();
        var serviceTime2 = service.NowMsk();
        
        // Assert
        Assert.True(serviceTime1 < serviceTime2);
    }
}