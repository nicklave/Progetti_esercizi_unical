import java.util.*;

import terminale.*;

public class GestioneParentele 
{	private ArrayList<String> parentele;
	
	public GestioneParentele()
	{	parentele = new ArrayList<>();
		parentele.add("Luigi A.");
		parentele.add("Francesco A.");
		parentele.add("Maria B.");
		parentele.add("Luigi A.");
		parentele.add("Giovanna C.");
		parentele.add("Paolo B.");
		parentele.add("Francesca D.");
		parentele.add("Francesco A.");
		parentele.add("Paola E.");
		parentele.add("Mario C.");
		parentele.add("Anna F.");
		parentele.add("Antonio B.");
		parentele.add("Simona G.");
		parentele.add("Giovanni D.");
		parentele.add("Maria H.");
	}
	
	public String nome(int i)
	{	return parentele.get(i);		
	}
	
	public int indicePadre(int i)
	{	return 2 * i + 1;		
	}
	
	public int indiceMadre(int i)
	{	return 2 * i + 2;		
	}
	
	public String nomePadre(int i)
	{	return nome(indicePadre(i));		
	}
	
	public String nomeMadre(int i)
	{	return nome(indiceMadre(i));		
	}
	
	public boolean genitoriMemorizzati(int i)
	{	return indiceMadre(i) < parentele.size();		
	}
	
	public ArrayList<String> nomiAscendenti(int i)
	{	ArrayList<String> ret = new ArrayList<>();
		if(!genitoriMemorizzati(i))
			return ret;
		ret.add(nomePadre(i));
		ret.add(nomeMadre(i));
		ret.addAll(nomiAscendenti(indicePadre(i)));
		ret.addAll(nomiAscendenti(indiceMadre(i)));
		return ret;		
	}
	
	public int contaAscendenti(int i)
	{	// soluzione 1 
		//return nomiAscendenti(i).size();
		
		// soluzione 2
		if(!genitoriMemorizzati(i))
			return 0;
		return 2 + contaAscendenti(indicePadre(i)) + contaAscendenti(indiceMadre(i)); 
	}
	
	public boolean eAscendente(int i1, int i2)
	{	return i1 == indicePadre(i2) || i1 == indiceMadre(i2) ||
				eAscendente(i1,indicePadre(i2)) || eAscendente(i1,indiceMadre(i2));
	}
}
