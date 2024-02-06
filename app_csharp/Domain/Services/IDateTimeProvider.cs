namespace Domain.Services;

/// <summary>
/// Date time retrieval
/// </summary>
public interface IDateTimeProvider
{
    /// <summary>
    /// Get now in Moscow Standard Time timezone
    /// </summary>
    DateTimeOffset NowMsk();
}