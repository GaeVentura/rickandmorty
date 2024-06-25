package src.Dispatcher;

import javax.jms.JMSException;
import javax.jms.MapMessage;
import javax.jms.Queue;
import javax.jms.QueueConnection;
import javax.jms.QueueSender;
import javax.jms.QueueSession;
import javax.jms.Session;

import src.Magazzino.iMagazzino;

public class DispatcherThread extends Thread{


    private iMagazzino mag;
    private QueueConnection qConn;
    private MapMessage mm;


    public DispatcherThread(iMagazzino mag, QueueConnection qConn, MapMessage mm){

        this.mag = mag;
        this.qConn = qConn;
        this.mm = mm;
    }
    


    public void run(){

        try {
            String op = mm.getString("operazione");
            Integer val = mm.getInt("valore");

            if (op.equalsIgnoreCase("deposita")){

                mag.deposita(val);
                QueueSession qSess = qConn.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
                QueueSender qSend = qSess.createSender((Queue) mm.getJMSReplyTo());

                MapMessage reply = qSess.createMapMessage();

                reply.setString("operazione", "risultato");
                reply.setString("risultato", "AGGIUNTA DEL VALORE: " + val.toString() + " ANDATA A BUON FINE");

                qSend.send(reply);

                qSend.close();
                qSess.close();

            } else if( op.equalsIgnoreCase("preleva")){
                
                Integer backValue = mag.preleva();
                QueueSession qSess = qConn.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
                QueueSender qSend = qSess.createSender((Queue) mm.getJMSReplyTo());

                MapMessage reply = qSess.createMapMessage();

                reply.setString("operazione", "risultato");
                reply.setString("risultato", "PRELEVATO VALORE: " + backValue.toString() + " ANDATA A BUON FINE");

                qSend.send(reply);

                qSend.close();
                qSess.close();

            } 

        } catch (JMSException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }

    }
}
