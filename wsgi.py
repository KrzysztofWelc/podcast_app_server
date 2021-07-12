from app import create_app

application = create_app(config='app.config.ProductionConfig')

if __name__ == "__main__":
 application.run()