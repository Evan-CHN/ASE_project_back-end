# A simple template for ASE project
## folder "routes"
Write route files, service functions will be put in "service" folder and we just call those service functions in "routes", besides in "routes", we are focusing how to present the appropriate structure of the response which can represent most of situations(e.g. success, error,missing...)
Here is an example code in this folder.
```python~~~~~~~~
class UserRoutes(Resource):
    def get(self):
        return {'code': 200, 'msg': 'ok', 'data': USER_LIST}
    def post(self):
        json_data = request.get_json()
        new_id = len(USER_LIST) + 1
        USER_LIST.append({'id': new_id, **json_data})
        return {'code': 204, 'msg': 'ok', 'data': USER_LIST[new_id-1]}
```
## folder "service"
write business logic.

## questions
1. Security Questions? Do we have to use some security framework to monitor some key functions like sign in, log out, sign up?
2. What kind of database do we want to use?
3. I want to make our backend to a pure RestfulAPI, which means reading frontend page should not be in our duty, so rendering pages is not our job right?
4. Since we have decided to add "sign in" function in our system, which means we will definitely use database, what kind of database we are going to use?
