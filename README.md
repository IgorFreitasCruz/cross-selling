

## Run the test suite with integration tests
- Docker will take some time to spin up the database container and prepare the data
> Note that to pass the option --integration we need to use -- otherwise Click would consider the option as belonging to the script ./manage.py instead of passing it as a pytest argument.
- All test receive the fixtures app_configuration, pg_session, and pg_test_data. The first fixture allows us to initialise the class PostgresRepo using the proper parameters. The second creates the database using the test data that is then contained in the third fixture.
```bash
~/cross_selling: ./manage.py test -- --integration
```

