from workers import WorkerEntrypoint, Response


#class Default(WorkerEntrypoint):
#    async def fetch(self, request):
#        return Response("Hello world!")

#from jinja2 import Template








@app.get("/")
async def root():
    message = "This is an example of FastAPI with Jinja2 - go to /hi/<name> to see a template rendered"
    return {"message": message + "Sao không thấy gì vậy? Ok đi chứ?"}


@app.get("/hi/{name}")
async def say_hi(name: str):
    message = template.render(name=name)
    return {"message": message}


@app.get("/env")
async def env(req: Request):
    env = req.scope["env"]
    message = f"Here is an example of getting an environment variable: {env.MESSAGE}"
    return {"message": message}


class Default(WorkerEntrypoint):
    async def fetch(self, request):
        #import asgi
        from jinja2 import Template 
        from fastapi import FastAPI, Request
        app = FastAPI()
        
        #environment = jinja2.Environment()
        #template = environment.from_string("Hello, {{ name }}!")
        #template_str = "Hello, {{ name }}!"
        #template = Template(template_str)
        
        #return await asgi.fetch(app, request.js_object, self.env)
        
        template = Template("Hello, {{ name }}!")
        html = template.render(name="Cloudflare")

        return Response(html, headers={"Content-Type": "text/html"})

