package src.Dispatcher;

import javax.jms.MapMessage;
import javax.jms.Message;
import javax.jms.MessageListener;
import javax.jms.QueueConnection;

import src.Magazzino.iMagazzino;

public class DispatcherListener implements MessageListener {

    private QueueConnection qconn;
    private iMagazzino mag;

    public DispatcherListener(QueueConnection qConn, iMagazzino mag){
        
        this.qconn = qConn;
        this.mag = mag;

    }
    

    @Override

    public void onMessage(Message message){

        MapMessage mm = (MapMessage) message;

        DispatcherThread t = new DispatcherThread(mag, qconn, mm);
        t.start();

        

        
    }
}
