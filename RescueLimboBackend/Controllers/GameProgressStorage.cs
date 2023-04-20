using Microsoft.AspNetCore.Mvc;
using System.Text.Json;

namespace RescueLimboBackend.Controllers;

[ApiController]
[Route("rescuelimbo")]
public class GameProgressStorage : ControllerBase
{
    private ILogger<GameProgressStorage> _logger;
    public GameProgressStorage(ILogger<GameProgressStorage> logger)
    {
        _logger = logger;
    }

    [HttpGet("increase")]
    public void IncreateCount(string key)
    {
        Dictionary<string, int>? data;
        if (System.IO.File.Exists("data.json"))
        {
            data = JsonSerializer.Deserialize<Dictionary<string, int>>(System.IO.File.ReadAllText("data.json"));
        }
        else
        {
            data = new Dictionary<string, int>();
        }
        
        if (data == null)
        {
            data = new Dictionary<string, int>();
        }
        if (!data.ContainsKey(key))
        {
            data.Add(key, 0);
        }
        data[key]++;
        using (var writer = new System.IO.StreamWriter("data.json"))
        {
            writer.WriteLine(JsonSerializer.Serialize(data, new JsonSerializerOptions() { Encoder = System.Text.Encodings.Web.JavaScriptEncoder.UnsafeRelaxedJsonEscaping }));
            writer.Close();
        }
        _logger.LogInformation($"{key} count has been increased.");
    }

    [HttpGet("get")]
    public int GetCount(string key)
    {
        Dictionary<string, int>? data;
        if (System.IO.File.Exists("data.json"))
        {
            data = JsonSerializer.Deserialize<Dictionary<string, int>>(System.IO.File.ReadAllText("data.json"));
            if (data != null)
            {
                if (data.ContainsKey(key))
                {
                    return data[key];
                }
            }
        }
        return 0;
    }
}
