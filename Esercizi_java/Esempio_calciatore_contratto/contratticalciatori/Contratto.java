package contratticalciatori;

import java.util.*;

public class Contratto 
{	private String squadra;
	private String calciatore;
	private int prezzo;
	private LinkedList<Integer> premi;
	
	public Contratto(String squadra, String calciatore, int prezzo, LinkedList<Integer> premi) 
	{	this.squadra = squadra;
		this.calciatore = calciatore;
		this.prezzo = prezzo;
		this.premi = new LinkedList<>(premi);
	}
	
	public String getSquadra() 
	{	return squadra;
	}
	
	public String getCalciatore() 
	{	return calciatore;
	}
	
	public int getPrezzo() 
	{	return prezzo;
	}
	
	public LinkedList<Integer> getPremi() 
	{	return new LinkedList<>(premi);
	}
	
	public boolean equals(Object o)
	{	if(o == null)
			return false;
		if(o == this)
			return true;
		if(!(o instanceof Contratto))
			return false;
		Contratto c = (Contratto)o;
		return squadra.equals(c.squadra) && calciatore.equals(calciatore);
	}
	
	public String toString()
	{	return "Acquisto di "+calciatore+" da parte della squadra "+squadra;
	}
}
