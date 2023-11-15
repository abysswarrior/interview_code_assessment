# interview_code_assessment
This is a test project for interview

# Run Locally

**Step 1 :** create a new virtualenv and install requirements.

```shell
$ pip install -r requirements.txt
```

**Note** : You can use `db.sqlight`. it has some data on it for testing. this data includes:

- a `admin` user [pass: admin]
- a `user1` user [pass: 1234]
- a `user2` user [pass: 1234]

also some articles and scores.

# Documentation

I use `drf-spectacular` for documentation. You can use [this](http://localhost:8000/schema/redoc/) or [this](http://localhost:8000/schema/swagger-ui/)
to see the doc. or you can use postman collection in `doc` directory.