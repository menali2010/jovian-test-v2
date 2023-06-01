from sqlalchemy import create_engine,text
fb_connection_string = ("mysql+pymysql://yf79e5e3bvwp1wx65mdc:pscale_pw_ez6A8XKaGa9b4vU1s7f30XWeOBSvxmt56juAIf0IVg3@aws.connect.psdb.cloud/leandrocareers?charset=utf8mb4")

engine = create_engine(db_connection_string, connect_args={
  "ssl":{
    "ssl_ca":"/etc/ssl/cert.pem",
  }
})

with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))
  print (result.all())