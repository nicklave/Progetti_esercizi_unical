public class Giocatore //LA CLASSE GENERA OGGETTI IMMUTABILI
{	private String nome;
	private String cognome;
	private int annoNascita;
	
	public Giocatore(String nome, String cognome, int annoNascita)
	{	this.nome = nome;
		this.cognome = cognome;
		this.annoNascita = annoNascita;		
	}
	
	public String getNome()
	{	return nome;		
	}
	
	public String getCognome()
	{	return cognome;		
	}
	
	public int getAnnoNascita()
	{	return annoNascita;		
	}
	
	public boolean eGiovane()
	{	return annoNascita > 1992;		
	}
	
	public String toString()
	{	return nome+" "+cognome+" nato nel "+annoNascita;		
	}
	
	public boolean equals(Object o)
	{	if(o == null)
			return false;
		if(o == this)
			return true;
		if(!(o instanceof Giocatore))
			return false;
		Giocatore g = (Giocatore)o;
		return nome.equals(g.nome) && cognome.equals(g.cognome) && annoNascita == g.annoNascita;
	}
}
