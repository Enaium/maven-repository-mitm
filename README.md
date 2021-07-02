# UrlRedirect

Default Config

```json
{
    "host": "0.0.0.0",
    "port": "14514",
    "redirect": [
        {
            "before": "https://repo1.maven.org/maven2",
            "after": "https://maven.aliyun.com/nexus/content/groups/public"
        },
        {
            "before": "https://repo.maven.apache.org/maven2",
            "after": "https://maven.aliyun.com/nexus/content/groups/public"
        },
        {
            "before": "https://jcenter.bintray.com",
            "after": "https://maven.aliyun.com/nexus/content/groups/public"
        }
    ]
}
```

Certificate Download

http://mitm.it/