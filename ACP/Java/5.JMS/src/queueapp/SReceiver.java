package queueapp;

import java.util.Hashtable;

import javax.jms.*;
import javax.naming.*;

public class SReceiver {

	public static void main(String[] args) {

		Hashtable<String,String> prop = new Hashtable<String,String>();

		prop.put("java.naming.factory.initial","org.apache.activemq.jndi.ActiveMQInitialContextFactory");
		prop.put("java.naming.provider.url","tcp://127.0.0.1:61616");
        prop.put("queue.test", "mytestqueue");


        TextMessage message;

        try {
            Context jndiContext = new InitialContext(prop);
            Queue queue = (Queue) jndiContext.lookup("test");
            QueueConnectionFactory queueConnectionFactory = (QueueConnectionFactory) jndiContext.lookup("QueueConnectionFactory");

            QueueConnection queueConn = queueConnectionFactory.createQueueConnection();
            queueConn.start();
            QueueSession queueSession = queueConn.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
            QueueReceiver receiver = queueSession.createReceiver(queue);


            do{

                message = (TextMessage) receiver.receive();

            } while (message.getText().equalsIgnoreCase("fine"));

            receiver.close();
            queueSession.close();
            queueConn.close();

        } catch(Exception e){
            e.printStackTrace();
        }

	}

}