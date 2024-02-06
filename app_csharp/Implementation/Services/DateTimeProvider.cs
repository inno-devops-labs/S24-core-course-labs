using Domain.Services;

namespace Implementation.Services;

/// <inheritdoc />
public class DateTimeProvider : IDateTimeProvider
{
    public DateTimeOffset NowMsk()
    {
        var mskTimezone = TimeZoneInfo.FindSystemTimeZoneById("Europe/Moscow");
        var mskTime = TimeZoneInfo.ConvertTime(DateTimeOffset.Now, mskTimezone);
        return mskTime;
    }
}