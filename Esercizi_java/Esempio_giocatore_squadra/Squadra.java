import java.util.*;

public class Squadra // LA CLASSE GENERA OGGETTI MUTABILI
{	private String nome;
	private ArrayList<Giocatore> giocatori;
	
	public Squadra(String nome)
	{	this.nome = nome;
		giocatori = new ArrayList<>();		
	}
	
	public Squadra(Squadra s)
	{	nome = s.nome;
		giocatori = new ArrayList<>(s.giocatori); // PROTECTIVE COPY
	}
	
	public String getNome()
	{	return nome;		
	}
	
	public ArrayList<Giocatore> getGiocatori()
	{	return new ArrayList<>(giocatori);	// PROTECTIVE COPY	
	}
	
	public Giocatore getGiocatorePosizione(int i)
	{	return giocatori.get(i);		
	}
	
	public void aggiungiGiocatore(Giocatore g)
	{	giocatori.add(g);		
	}
	
	public void rimuoviGiocatorePosizione(int i)
	{	giocatori.remove(i);		
	}
	
	public void sostituisciGiocatorePosizione(Giocatore g, int i)
	{	giocatori.set(i, g);
	}
	
	public boolean contiene(Giocatore g)
	{	return giocatori.contains(g);		
	}
	
	public String toString()
	{	String ret = "*** "+nome+" ***\n";
		for(Giocatore g : giocatori)
			ret += g+"\n";
		ret += "******";
		return ret;		
	}
	
	public boolean equals(Object o)
	{	if(o == null)
			return false;
		if(o == this)
			return true;
		if(!(o instanceof Squadra))
			return false;
		Squadra s = (Squadra)o;
		return nome.equals(s.nome) && giocatori.equals(s.giocatori);
	}
}
