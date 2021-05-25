using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class IAAC_ToggleLine_Demo : MonoBehaviour
{
public GameObject lineGameobject;
public IAAC_DrawLine_GP1 lineComponent;

bool flag = false;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {

        if(GetForceCondition() && !flag)
        {      
              lineGameobject.GetComponent<IAAC_DrawLine_GP1>().ToggleLineStart1();
              flag = true;
       // lineComponent.ToggleLineStart1();

        }
        else if (!GetForceCondition() && flag)
        {
           lineGameobject.GetComponent<IAAC_DrawLine_GP1>().ToggleLineStart1();
           flag = false;
    

        }
    


    }
    private bool GetForceCondition()
    {
        // for demo Y pos  -> real Force
        return (transform.position.y >1);


    }
}
