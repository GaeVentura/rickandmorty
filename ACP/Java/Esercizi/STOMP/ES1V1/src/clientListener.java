

import javax.jms.JMSException;
import javax.jms.MapMessage;
import javax.jms.Message;
import javax.jms.MessageListener;

public class clientListener implements MessageListener{

    @Override
    public void onMessage(Message message){

        MapMessage mm = (MapMessage) message;

        String operazione;
        try {
            operazione = mm.getString("operazione");

            if(operazione.equalsIgnoreCase("deposita")){

                String risultato = mm.getString("risultato");
    
                System.out.println("[CLIENT] IL RISULTATO DEL DEPOSITO: "+risultato);
                
    
            } else if(operazione.equalsIgnoreCase("preleva")){

                Integer valore = mm.getInt("valore");

                System.out.println("[CLIENT] IL VALORE RICEVUTO E' "+valore);
                
            }
        } catch (JMSException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }



        
    }
    
}
