package contratticalciatori;

import java.util.*;

public class Sistema 
{	private LinkedList<Calciatore> calciatori;
	private LinkedList<Contratto> contratti;

	public Sistema(LinkedList<Calciatore> calciatori, LinkedList<Contratto> contratti)
	{	this.calciatori = new LinkedList<Calciatore>(calciatori);
		this.contratti = new LinkedList<Contratto>(contratti);
	}
	
	public boolean verificaDati()
	{	for(Contratto c : contratti)
		{	String squadraAttuale = trovaCalciatore(c.getCalciatore()).getSquadraAttuale();
			if(squadraAttuale.equals(c.getSquadra()))
				return false;		
		}
		return true;
	}
	
	private Calciatore trovaCalciatore(String nome)
	{	for(Calciatore c : calciatori)
			if(c.getNome().equals(nome))
				return c;
		return null;
	}
	
	public LinkedList<String> squadreAttive(int pMin)
	{	LinkedList<String> ret = new LinkedList<>();
		LinkedList<String> nomiSquadre = estraiSquadre();
		for(String nomeSquadra : nomiSquadre)
			if(numSquadreAcquisti(nomeSquadra) >= 3
					&& spesaTotale(nomeSquadra) >= pMin)
				ret.addLast(nomeSquadra);
		return ret;
	}
	
	private LinkedList<String> estraiSquadre()
	{	LinkedList<String> ret = new LinkedList<>();
		for(Contratto c : contratti)
		{	String nomeSquadra = c.getSquadra();
			if(!ret.contains(nomeSquadra))
				ret.addLast(nomeSquadra);
		}
		return ret;		
	}
	
	private int numSquadreAcquisti(String nomeSquadra)
	{	LinkedList<String> ret = new LinkedList<>();
		for(Contratto c : contratti)
			if(c.getSquadra().equals(nomeSquadra))
			{	String nomeCalciatore = c.getCalciatore();
				String squadraAttuale = trovaCalciatore(nomeCalciatore).getSquadraAttuale();
				if(!ret.contains(squadraAttuale))
					ret.addLast(squadraAttuale);
			}
		return ret.size();
	}
	
	private int spesaTotale(String nomeSquadra)
	{	int somma = 0;
		for(Contratto c : contratti)
			if(c.getSquadra().equals(nomeSquadra))
				somma += c.getPrezzo();
		return somma;		
	}
	
	public LinkedList<String> calciatoriPocoPremiati(int pMax)
	{	LinkedList<String> ret = new LinkedList<>();
		for(Contratto c : contratti)
		{	LinkedList<Integer> premi = c.getPremi();
			if(nonSuperiori(premi,pMax))
				ret.addLast(c.getCalciatore());
		}
		return ret;
	}
	
	private boolean nonSuperiori(LinkedList<Integer> lista, int valore)
	{	for(int e : lista)
			if(e > valore)
				return false;
		return true;
	}
	
}
