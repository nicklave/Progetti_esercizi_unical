package conticorrenti;

import java.util.*;

public class Banca // LA CLASSE GENERA OGGETTI MUTABILI
{	private ArrayList<ContoCorrente> contiCorrenti;

	public Banca()
	{	contiCorrenti = new ArrayList<>();		
	}
	
	public Banca(Banca b)
	{	contiCorrenti = new ArrayList<>(b.contiCorrenti);		
	}
	
	public void aggiungiContoCorrente(ContoCorrente c)
	{	contiCorrenti.add(new ContoCorrente(c));		
	}
	
	public int numeroContiCorrenti()
	{	return contiCorrenti.size();		
	}
	
	public ContoCorrente cerca(String IBAN)
	{	for(ContoCorrente c : contiCorrenti)
			if(c.getIBAN().equals(IBAN))
				return new ContoCorrente(c);
		return null;	
	}
	
	public String clienteContoMax()
	{	ContoCorrente contoMax = contiCorrenti.get(0);
		float saldoMax = contoMax.getSaldoContabile();
		for(int i = 1; i < contiCorrenti.size(); i++)
		{	float saldo = contiCorrenti.get(i).getSaldoContabile();
			if(saldo > saldoMax)
			{	contoMax = contiCorrenti.get(i);
				saldoMax = saldo;
			}
		}
		return contoMax.getIntestatario();
	}
	
	public int contaDepositi()
	{	int cont = 0;
		for(ContoCorrente c : contiCorrenti)
			for(Movimento m : c.getMovimenti())
				if(m.getTipo().equals("deposito"))
					cont++;
		return cont;		
	}
	
	public ArrayList<ContoCorrente> cercaContiSenzaMovimentiTipo(String tipo)
	{	ArrayList<ContoCorrente> ret = new ArrayList<>();
		for(ContoCorrente c : contiCorrenti)
			if(!contieneMovimentiTipo(c,tipo))
				ret.add(new ContoCorrente(c));
		return ret;		
	}
	
	private boolean contieneMovimentiTipo(ContoCorrente c, String tipo)
	{	for(Movimento m : c.getMovimenti())
			if(m.getTipo().equals(tipo))
				return true;
		return false;
	}

}
