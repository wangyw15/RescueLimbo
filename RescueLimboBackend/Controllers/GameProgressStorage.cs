using Microsoft.AspNetCore.DataProtection.KeyManagement;
using Microsoft.AspNetCore.Mvc;
using System.Text.Json;

namespace RescueLimboBackend.Controllers;

[ApiController]
[Route("rescuelimbo")]
public class GameProgressStorage : ControllerBase
{
	private readonly DataStorageService _data;
	private ILogger<GameProgressStorage> _logger;
    public GameProgressStorage(ILogger<GameProgressStorage> logger, DataStorageService dataService)
    {
        _logger = logger;
        _data = dataService;
    }

    [HttpGet("increase")]
    public void IncreateCount(string key)
    {
        _data.SetValue(key, _data.GetValue(key) + 1);
		_logger.LogInformation($"{key} count has been increased.");
	}

    [HttpGet("get")]
    public int GetCount(string key)
	{
		_logger.LogInformation($"query {key} counts.");
		return _data.GetValue(key);
	}

    [HttpGet("get_all")]
    public Dictionary<string, int> GetAllCount()
	{
		_logger.LogInformation("query all counts.");
		var ret = new Dictionary<string, int>();
		foreach (var item in _data.GetAll())
        {
            ret.Add(item.Key, item.Value);
        }
        return ret;
    }
}
