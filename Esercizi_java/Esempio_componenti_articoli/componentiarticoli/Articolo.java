package componentiarticoli;

import java.util.*;

public class Articolo 
{	private String nome;
	private float prezzo;
	private LinkedList<String> componenti;
	
	public Articolo(String nome, float prezzo, LinkedList<String> componenti) 
	{	this.nome = nome;
		this.prezzo = prezzo;
		this.componenti = new LinkedList<>(componenti);
	}
	
	public String getNome() 
	{	return nome;
	}
	
	public float getPrezzo() 
	{	return prezzo;
	}
	
	public LinkedList<String> getComponenti() 
	{	return new LinkedList<>(componenti);
	}
	
	public String toString()
	{	return "Articolo con nome "+nome+", componenti "+componenti+" e prezzo "+prezzo;		
	}
	
	public boolean equals(Object o)
	{	if(o == null)
			return false;
		if(o == this)
			return true;
		if(!(o instanceof Articolo))
			return false;
		Articolo a = (Articolo)o;
		return nome.equals(a.getNome());
	}
}
