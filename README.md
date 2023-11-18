# Cross-selling API

<br>

## Run the test suite with integration tests
- Docker will take some time to spin up the database container and prepare the data
> Note that to pass the option --integration we need to use -- otherwise Click would consider the option as belonging to the script ./manage.py instead of passing it as a pytest argument.
- All test receive the fixtures app_configuration, pg_session, and pg_test_data. The first fixture allows us to initialise the class PostgresRepo using the proper parameters. The second creates the database using the test data that is then contained in the third fixture.
```bash
~/cross_selling: ./manage.py test -- --integration
```

<br>

## Build a web stack for production
> I forced the variable APPLICATION_CONFIG to be production if not specified in `manage.py`
- Building the container
```bash
~/cross_selling: ./manage.py compose build web
```

<br>

- If this is successful you can run Docker Compose
```bash
~/cross_selling: ./manage.py compose up -d
```
and the output of `docker ps` should show three containers running.

<br>

- Connect to a Postgres batabase with configurations set in `config/production.json`. **You only need to run this command once!**
```bash
~/cross_selling: ./manage.py init-postgres
```
if the command executes successfully no messge will appear. If a database already exists you will see `The database cross_selling_db already exists and will not be created`

<br>

- Check what this command did connect to the database. Do it executing psql in the database container
```bash
~/cross_selling: ./manage.py compose exec db psql -U postgres
```
specify the user `-U postgres` that is the user created through the variable `POSTGRES_USER` in `config/production.json`.
```bash
# you should see this line in the terminal
postgres=#
```


## Tear down the system running
```bash
~/cross_selling: ./manage.py compose down
```
