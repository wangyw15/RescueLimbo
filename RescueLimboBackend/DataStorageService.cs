using LiteDB;

namespace RescueLimboBackend;

public class KeyValue
{
	[BsonId]
	public string Key { get; set; }
	public int Value { get; set; }

	public KeyValue(string name, int value)
	{
		Key = name;
		Value = value;
	}
}

public class DataStorageService
{
    private LiteDatabase _database;
    private ILiteCollection<KeyValue> _data;

    public DataStorageService()
    {
        _database = new LiteDatabase("data.db");
        _data = _database.GetCollection<KeyValue>("data");
        _data.EnsureIndex(x => x.Key, true);
    }

    public void SetValue(string key, int value) => _data.Upsert(new KeyValue(key, value));
    
    public int GetValue(string key)
    {
        var query = _data.Find(x => x.Key == key);
        if (query.Any())
        {
            return query.First().Value;
        }
        return 0;
    }

    public IEnumerable<KeyValue> GetAll() => _data.FindAll();


	~DataStorageService()
    {
        _database.Commit();
        _database.Dispose();
    }
}
