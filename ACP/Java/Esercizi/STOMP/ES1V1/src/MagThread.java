
import javax.jms.JMSException;
import javax.jms.MapMessage;
import javax.jms.Queue;
import javax.jms.QueueConnection;
import javax.jms.QueueSender;
import javax.jms.QueueSession;
import javax.jms.Session;



public class MagThread extends Thread {

    private MapMessage mm;

    private CodaWrapperSem coda;

    private QueueConnection qConn;


    public MagThread(MapMessage mm, CodaWrapperSem coda, QueueConnection qConn){

        this.mm = mm;
        this.coda = coda;
        this.qConn = qConn;
    }

    public void run(){

        String operazione;

        try {

            operazione = mm.getString("operazione");
            QueueSession qSes = qConn.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);

            QueueSender qSender = qSes.createSender((Queue) mm.getJMSReplyTo());
            System.out.println(operazione);
            if(operazione.equalsIgnoreCase("deposita")){

                coda.inserisci(mm.getInt("valore"));
                System.out.println("arrivo qui");
                MapMessage backMapMessage = qSes.createMapMessage();

                backMapMessage.setString("operazione", "deposita");
                backMapMessage.setString("risultato", "DEPOSITATO");
                qSender.send(backMapMessage);


                qSender.close();
                qSes.close();


    
            } else if(operazione.equalsIgnoreCase("preleva")){

                Integer valore = coda.preleva();

                System.out.print("il valore che ho preso è" + valore);
                MapMessage backMapMessage = qSes.createMapMessage();
                
                backMapMessage.setString("operazione", "preleva");
                backMapMessage.setInt("valore", valore);

                qSender.send(backMapMessage);

                qSender.close();
                qSes.close();

                
            }
        } catch (JMSException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }


    }

}
