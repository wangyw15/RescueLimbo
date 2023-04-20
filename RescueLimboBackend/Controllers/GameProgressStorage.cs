using Microsoft.AspNetCore.Mvc;


namespace RescueLimboBackend.Controllers;

[ApiController]
[Route("[controller]")]
public class GameProgressStorage : ControllerBase
{
    [HttpGet(Name = "increase")]
    public void IncreaseCountByKey(string key)
    {
        Console.WriteLine($"{key} count has been increased.");
        // [TODO)
    }
}
