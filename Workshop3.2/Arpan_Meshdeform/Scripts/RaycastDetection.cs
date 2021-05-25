using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class RaycastDetection : MonoBehaviour
{
   
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {

    }

    private void OnDrawGizmos()
    {
        float maxDistance = 20f;
        RaycastHit hit;

        bool isHit = Physics.Raycast(origin: transform.position, direction: transform.forward, out hit, maxDistance);
        if (isHit)
        {
            Gizmos.color = Color.red;
            Gizmos.DrawRay(from: transform.position, direction: transform.forward * hit.distance);
            Debug.LogError(hit.distance);
        }
        else
        {
            Gizmos.color = Color.green;
            Gizmos.DrawRay(from: transform.position, direction: transform.forward * maxDistance);
        }
    }
}
