package manutenzione;

import java.util.*;

public class Intervento 
{	private String nomeTecnico;
	private LinkedList<String> tipiOperazione;
	private int data;
	private int durata;
	
	public Intervento(String nomeTecnico, LinkedList<String> tipiOperazione, int data, int durata) 
	{	this.nomeTecnico = nomeTecnico;
		this.tipiOperazione = new LinkedList<String>(tipiOperazione);
		this.data = data;
		this.durata = durata;
	}
	
	public String getNomeTecnico() 
	{	return nomeTecnico;
	}
	
	public LinkedList<String> getTipiOperazione() 
	{	return new LinkedList<String>(tipiOperazione);
	}
	
	public int getData() 
	{	return data;
	}
	
	public int getDurata() 
	{	return durata;
	}
	
	public boolean equals(Object o)
	{	if(o == null)
			return false;
		if(o == this)
			return true;
		if(!(o instanceof Tecnico))
			return false;
		Intervento i = (Intervento)o;
		return nomeTecnico.equals(i.nomeTecnico) && tipiOperazione.equals(i.tipiOperazione) &&
				data == i.data && durata == i.durata;
	}
}
