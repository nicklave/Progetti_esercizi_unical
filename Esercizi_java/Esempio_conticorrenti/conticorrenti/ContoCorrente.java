package conticorrenti;

import java.util.*;

public class ContoCorrente //LA CLASSE GENERA OGGETTI MUTABILI
{	private String IBAN;
	private String intestatario;
	private ArrayList<Movimento> movimenti;
	private float fido;
	
	public ContoCorrente(String IBAN, String intestatario)
	{	this.IBAN = IBAN;
		this.intestatario = intestatario;
		movimenti = new ArrayList<>();
		fido = 0;
	}
	
	public String getIBAN()
	{	return IBAN;		
	}
	
	public String getIntestatario()
	{	return intestatario;		
	}
	
	public ArrayList<Movimento> getMovimenti() {
		return new ArrayList<Movimento>(movimenti);
	}

	public float getFido() {
		return fido;
	}

	public ContoCorrente(ContoCorrente c)
	{	IBAN = c.IBAN;
		intestatario = c.intestatario;
		movimenti = new ArrayList<>(c.movimenti);
		fido = c.fido;		
	}
	
	public void setFido(float fido)
	{	this.fido = fido;		
	}
	
	public void aggiungiMovimento(Movimento m)
	{	movimenti.add(m);		
	}
	
	public float getSaldoContabile()
	{	float somma = 0;
		for(Movimento m : movimenti)
			somma += m.getValore();
		return somma;
	}
	
	public float getSaldoDisponibile()
	{	return getSaldoContabile() + fido;		
	}
	
	public String toString()
	{	String ret = "";
		ret += "Conto con codice IBAN "+IBAN+" intestato a "+intestatario+"\n";
		if(fido > 0)
			ret += "Fido: "+fido+"\n";
		ret += "Saldo contabile: "+getSaldoContabile()+"\n";
		ret += "Saldo disponibile: "+getSaldoDisponibile()+"\n";
		if(!movimenti.isEmpty())
		{	ret += "Lista dei movimenti:\n";
			for(Movimento m : movimenti)
				ret += m + "\n";
		}
		return ret;		
	}
	
	public boolean equals(Object o)
	{	if(o == null)
			return false;
		if(o == this)
			return true;
		if(!(o instanceof ContoCorrente))
			return false;
		ContoCorrente c = (ContoCorrente)o;
		return IBAN.equals(c.IBAN);
	}
	
	
}
