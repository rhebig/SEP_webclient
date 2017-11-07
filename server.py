import os
import json
import tornado.ioloop
import tornado.web

ROOT = os.path.dirname(__file__)
PORT = 8888

class IndexHandler(tornado.web.RequestHandler):
    """ Handles request for the main page"""
    def get(self):
        self.render("index.html")

class LoginHandler(tornado.web.RequestHandler):
    """ Handles request for the login page"""
    def get(self):
        self.render("login.html")

class AccountHandler(tornado.web.RequestHandler):
    """ Handles requests for the account page"""
    def get(self):
        self.render("account.html")

class FileSystemHandler(tornado.web.RequestHandler):
    """ Queries the file structur and return the filesystem represented as a JSON String"""
    def get(self):
        filesystem = {"a": {"id":"a","parent": "b","type": "folder","name": "Folder-A","lastModified": "2011-07-15","children": ["f", "g"],"status":"open","user":["reem"],"owner":"mazen"},"b": {"id":"b","parent": "null","type": "folder","name": "Folder-B","lastModified": "1999-07-15","children": ["a", "c", "d"],"status":"open","user":["mazen"],"owner":"reem"},"d": {"id":"d","parent": "b","type": "folder","name": "Folder-D","lastModified": "2000-07-15","children": [],"status":"open","user":["mazen","peter"],"owner":"calle"},"f": {"id":"f","parent": "a","type": "folder","name": "folder-F","lastModified": "2017-07-15","children": ["c", "h"],"status":"closed","user":["emil"],"owner":"joushua"},"c": {"id":"c","parent": "f","type": "folder","name": "folder-C","lastModified": "2017-07-15","children": [],"status":"open","user":["mazen"],"owner":"peter"},"g": {"id":"g","parent": "a","type": "folder","name": "Folder-G","lastModified": "2017-10-15","children": [],"status":"open","user":["mazen"],"owner":"joushua"},"h": {"id":"h","parent": "f","type": "folder","name": "Folder-H","lastModified": "2017-10-15","children": ["i"],"status":"closed","user":["mazen","emil"],"owner":"peter"},"i": {"id":"i","parent": "h","type": "folder","name": "Folder-I","lastModified": "2017-10-15","children": ["j"],"status":"closed","user":[],"owner":"mazen"},"j": {"id":"j","parent": "i","type": "folder","name": "Folder-J","lastModified": "2017-10-15","children": ["k"],"status":"open","user":["reem","mazen"],"owner":"mazen"},"k": {"id":"k","parent": "j","type": "folder","name": "Folder-K","lastModified": "2017-10-12","children": ["l", "m"],"status":"closed","user":["calle","peter","mazen"],"owner":"joushua"},"l": {"id":"l","parent": "k","type": "folder","name": "Folder-L","lastModified": "2017-09-15","children": [],"status":"open","user":["mazen"],"owner":"joushua"},"m": {"id":"m","parent": "k","type": "File","name": "Folder-M","lastModified": "2017-09-15","children": [],"status":"open","user":["mazen"],"owner":"peter" ,"project_id":"project1"},"cad1": {"id":"cad1","parent": "k","type": "File","name": "CAD1-M","lastModified": "2017-09-15","children": [],"status":"open","user":["mazen"],"owner":"peter","project_id":"project1","extention": "CAD"},"stl1": {"id":"stl1","parent": "k","type": "File","name": "STL1-M","lastModified": "2017-09-15","children": [],"status":"open","user":["mazen"],"owner":"peter","project_id":"project1","extention": "STL"},"build1": {"id":"build1","parent": "k","type": "File","name": "Build1","lastModified": "2017-09-15","children": [],"status":"open","user":["mazen"],"owner":"peter","project_id":"project1","extention": "build"},"build2": {"id":"build2","parent": "k","type": "File","name": "Build2","lastModified": "2017-09-15","children": [],"status":"open","user":["mazen"],"owner":"peter","project_id":"project1","extention": "build"},"material1":{"type":"File","id": "material1","project_id":"project1" ,"build_id":"build1" ,"name":"material1","extention": "material"},"material2":{"type":"File","id": "material2","project_id":"project1" ,"build_id":"build2" ,"name":"material2","extention": "material"} ,"customer1":{"name":"Volvo","project_id":"project1","id":"customer1","extention": "customer"},"project1":{"type":"File","name":"P01","id":"project1","extention": "project"},"measure1":{"type":"File","id": "measure1","project_id":"project1","build_id":"build1","material_id":"material1","name":"material1 measure","certificate":"m","extention":"measure"},"measure2":{"type":"File","id": "measure2","project_id":"project1","build_id":"build2","material_id":"material2","name":"material2 measure","certificate":"m","extention":"measure"},"image1":{"type":"File","id": "image1","project_id":"project1","build_id":"build1","name":"image1","certificate":"m","extention":"image"},"image2":{"type":"File","id": "image2","project_id":"project1","build_id":"build2","name":"image2","certificate":"m","extention":"image"},"slm1":{"type":"File","id": "slm1","project_id":"project1","build_id":"build1","name":"SLM1","extention":"SLM"} ,"slm2":{"type":"File","id": "slm2","project_id":"project1","build_id":"build1","name":"SLM2","extention":"SLM"},"slm3":{"type":"File","id": "slm3","project_id":"project1","build_id":"build2","name":"SLM3","extention":"SLM"}}
        self.write(json.dumps({"status":"ok", "sent":filesystem}))

def make_app():
    """ Defines settings and routes. Returns an application"""
    return tornado.web.Application(
        # path to scripts, img, etc.
        static_path=os.path.join(ROOT, "static"),
        # path to html files
        template_path=os.path.join(ROOT, "templates"),
        # set routes and specify handlers
        handlers=[
            (r"/", IndexHandler),
            (r"/login", LoginHandler),
            (r"/account", AccountHandler),
            (r"/filesystem", FileSystemHandler)
        ])

if __name__ == "__main__":
    print ("Server started")
    APP = make_app()
    APP.listen(PORT)
    tornado.ioloop.IOLoop.current().start()
    