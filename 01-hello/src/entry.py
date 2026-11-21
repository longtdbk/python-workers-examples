from workers import WorkerEntrypoint, Response

class Default(WorkerEntrypoint):
    async def fetch(self, request):
        import asgi
        from jinja2 import Template 
        from fastapi import FastAPI, Request

        
        #environment = jinja2.Environment()
        #template = environment.from_string("Hello, {{ name }}!")
        #template_str = "Hello, {{ name }}!"
        #template = Template(template_str)
        
        #return await asgi.fetch(app, request.js_object, self.env)
        
        template = Template("Hello, {{ name }}!")
        html = template.render(name="Cloudflare")

        return Response(html, headers={"Content-Type": "text/html"})

