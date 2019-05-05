import evebot
import asyncio
import traceback
from models import User, Chat, Server, Service, Session, get_or_create

# A local client for testing commands out
def run():
    eve = evebot.EveBot(User(id=0, username="Eve"))

    if(eve):
        
        async def sendReply(text,*args,**kwargs):
            print("Eve: " + text)

        print("Running Locally")
        loop = asyncio.get_event_loop()

        while(1):
            session = Session()
            service = get_or_create(session, Service,name="local")
            current_user = get_or_create(session, User, service_id=service.id, id=0, username="Me")

            current_server = get_or_create(session, Server, service_id=service.id, id=0, server_name="Local Server")

            current_channel = get_or_create(session, Chat, server_id=current_server.id, id=0, chat_name="Local Channel")

            metadata = {"session":session, "service": service, "user":current_user, "server":current_server, "chat":current_channel}

            message = input()

            try:
                loop.run_until_complete(eve.read(message, metadata, sendReply))
            except Exception as e:
                print("Exception: " + str(e))
                print(traceback.print_exc())
            
            try:
                session.commit()
            except:
                session.rollback()
            finally:
                session.close()
        loop.close()

if __name__ == "__main__":
    run()
