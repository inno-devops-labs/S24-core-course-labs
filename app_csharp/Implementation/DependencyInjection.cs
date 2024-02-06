using Domain.Services;
using Implementation.Services;
using Microsoft.Extensions.DependencyInjection;

namespace Implementation;

public static class DependencyInjection
{
    public static void AddServices(this IServiceCollection serviceCollection)
    {
        serviceCollection.AddTransient<IDateTimeProvider, DateTimeProvider>();
    }
}