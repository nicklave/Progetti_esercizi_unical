package manutenzione;

import java.util.*;

public class Sistema 
{	private LinkedList<Tecnico> tecnici;
	private LinkedList<Intervento> interventi;

	public Sistema(LinkedList<Tecnico> tecnici,LinkedList<Intervento> interventi)
	{	this.tecnici = new LinkedList<Tecnico>(tecnici);
		this.interventi = new LinkedList<Intervento>(interventi);
	}
	
	public Tecnico tecnicoMax()
	{	Tecnico tecnicoMax = null;
		int maxCostoComplessivo = 0;
		for(Tecnico t : tecnici)
		{	int costoComplessivoT = costoComplessivo(t);
			if(costoComplessivoT > maxCostoComplessivo)
			{	tecnicoMax = t;
				maxCostoComplessivo = costoComplessivoT;				
			}
		}
		return tecnicoMax;
	}
	
	private int costoComplessivo(Tecnico t)
	{	int sommaDurateInterventi = 0;
		for(Intervento i : interventi)
			if(i.getNomeTecnico().equals(t.getNome()))
				sommaDurateInterventi += i.getDurata();
		return sommaDurateInterventi * t.getCostoOrario();
	}
	
	public LinkedList<String> tecniciRiparatori(int r)
	{	LinkedList<String> ret = new LinkedList<>();
		for(Tecnico t : tecnici)
			if(contaInterventiConRiparazione(t.getNome()) >= r)
				ret.addLast(t.getNome());
		return ret;
	}
	
	private int contaInterventiConRiparazione(String nomeTecnico)
	{	int c = 0;
		for(Intervento i : interventi)
			if(i.getNomeTecnico().equals(nomeTecnico) && i.getTipiOperazione().contains("Riparazione"))
				c++;
		return c;		
	}
	
	public LinkedList<String> tecniciJolly(int cm, int d1, int d2, int t)
	{	LinkedList<String> ret = new LinkedList<>();
		for(Tecnico tec : tecnici)
			if(tec.getCostoOrario() <= cm && tipiDiversiOperazioni(tec.getNome(), d1, d2, t))
				ret.addLast(tec.getNome());
		return ret;
	}
	
	private boolean tipiDiversiOperazioni(String nomeTecnico, int d1, int d2, int t)
	{	LinkedList<Intervento> interventiDiInteresse = new LinkedList<>();
		for(Intervento i : interventi)
			if(i.getNomeTecnico().equals(nomeTecnico) && i.getData() >= d1 && i.getData() <= d2)
				interventiDiInteresse.addLast(i);
		LinkedList<String> tipiOperazioniDiversi = new LinkedList<>();
		for(Intervento i : interventiDiInteresse)
			for(String tipoOperazione : i.getTipiOperazione())
				if(!tipiOperazioniDiversi.contains(tipoOperazione))
					tipiOperazioniDiversi.addLast(tipoOperazione);
		return tipiOperazioniDiversi.size() >= t;		
	}
}
