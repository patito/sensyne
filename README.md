# Sensyne

## Start API

It will also run DB migration from `docker-entrypoint.sh`

```
# make up
```

## Notes

- Script `wait-for-it.sh` is opensource, so I just use it
- I did not add the OpenAPI (Flasgger), just did not have the time
- I could use Marshmallow to validate the input/schema
- The PUT (Update a single product) is a PATCH, they are not the same.
- POST /v1/product in my opinion should be /v1/products, we are adding a product to a collection
- GET /v1/product/id I also would use plural
- Long time I do not use flask also, lately have been working with aws chalice
- Sorry, I did not write the integration tests because of the time I spent discording with the API :),
you can find my tests and other projects in my gitlab (opensource). 
