using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class IAAC_DrawLine_GP1 : MonoBehaviour
{
    public GameObject ObjectToFollow1;
    public GameObject axisPrefab1;
    public float distanceForward1 = 0.2f;
    public float lineDistance1 = 0.01f;
    public GameObject lineRendPrefab1;
    public float lineWidth1 = 0.001f;
   public GameObject RobotTarget_MainGameobject;

    private GameObject axisInstantiate;
    private Vector3 endPoint;
    private bool paintingOn = false;
    private bool newPaintVerticies = false;
    private Vector3 previousPosition;
    private List<Vector3> currVerticies;
    private Color doodleColor;
    private GameObject myDoodleLineRend;
    private LineRenderer doodleLine;


    //GP1 Added
    
    public GameObject RoboTargetPrefab;
    private int ToolPathNumber;
    private GameObject RobotTargetInsance;    
    private GameObject robotPath;

    public GameObject ikModel;
    void Start()
    {
    


        ToolPathNumber = 0; 
        currVerticies = new List<Vector3>();
        doodleColor = Color.yellow;
    }

    void Update()
    {
        //This is for holding down touch and letting go on mobile
        /*
        if (Input.touchCount > 0)
        {
            var touch = Input.GetTouch(0);
            if (touch.phase == TouchPhase.Began && EventSystem.current.IsPointerOverGameObject(Input.GetTouch(0).fingerId) == false)
            {
                myDoodleLineRend = Instantiate(lineRendPrefab, Vector3.zero, Quaternion.identity);
                myDoodleLineRend.transform.parent = geometryParent.transform;
                doodleLine = myDoodleLineRend.GetComponent<LineRenderer>();
                doodleLine.material.color = doodleColor;
                doodleLine.startWidth = laserWidth;
                doodleLine.endWidth = laserWidth;
                paintingOn = true;
            }

            if (touch.phase == TouchPhase.Ended)
            {
                paintingOn = false;
                currVerticies = new List<Vector3>();
            }
        }
        */

        if (paintingOn)
        {
            Vector3 origin = ObjectToFollow1.transform.position;
            Vector3 direction = ObjectToFollow1.transform.TransformDirection(Vector3.forward);

            endPoint = origin + direction * distanceForward1;


            if (newPaintVerticies)
            {
                if (currVerticies.Count > 0)
                {
                    doodleLine.positionCount = currVerticies.Count;

                    for (int i = 0; i < currVerticies.Count; i++)
                    {
                        doodleLine.SetPosition(i, currVerticies[i]);
                    }
                    newPaintVerticies = false;
                }
            }

        }

        if (Vector3.Distance(endPoint, previousPosition) > lineDistance1)
        {
            if (paintingOn)
            {


                previousPosition = endPoint;
                newPaintVerticies = true;

                currVerticies.Add(endPoint);

                axisInstantiate = Instantiate(axisPrefab1, endPoint, ObjectToFollow1.transform.rotation);
                axisInstantiate.transform.RotateAround(axisInstantiate.transform.position, axisInstantiate.transform.right, 180);
                axisInstantiate.transform.localScale = new Vector3(.01f, .01f, .01f);
                axisInstantiate.transform.parent = myDoodleLineRend.transform;

                /*
                RobotTargetInsance = Instantiate(RoboTargetPrefab,endPoint,ObjectToFollow1.transform.rotation);
                RobotTargetInsance.transform.RotateAround(RobotTargetInsance.transform.position, RobotTargetInsance.transform.right, 180);
                RobotTargetInsance.transform.localScale = new Vector3(.01f, .01f, .01f);
                RobotTargetInsance.transform.parent = robotPath.transform;
                */



            }
        }

    }
    public void ToggleLineStart1()
    {
        paintingOn = !paintingOn;

        if (paintingOn)
        {
            myDoodleLineRend = Instantiate(lineRendPrefab1, Vector3.zero, Quaternion.identity);
            doodleLine = myDoodleLineRend.GetComponent<LineRenderer>();
            doodleLine.material.color = doodleColor;
            doodleLine.startWidth = lineWidth1;
            doodleLine.endWidth = lineWidth1;



        }
        else
        {
            ikModel.GetComponent<RosSharp_Kinematics>().RobotTarget_Parent_WorldSpace  = myDoodleLineRend;
            // Also call preview point
            /*
            setting the robot target parent as the last line
            send the point for IK model
            send to point to the FK model
            */
            currVerticies = new List<Vector3>();
        }
    }

    public void LineStart1()
    {
        paintingOn = true;

        myDoodleLineRend = Instantiate(lineRendPrefab1, Vector3.zero, Quaternion.identity);
        doodleLine = myDoodleLineRend.GetComponent<LineRenderer>();
        doodleLine.material.color = doodleColor;
        doodleLine.startWidth = lineWidth1;
        doodleLine.endWidth = lineWidth1;


        string layerName = string.Format("Robot_Path_{0}}",ToolPathNumber);
        robotPath = new GameObject(layerName);
        robotPath.transform.parent = RobotTarget_MainGameobject.gameObject.transform.parent;
 
    }

    public void LineStop1()
    {
        paintingOn = false;
        //take the point list and create a 
        LineToRobotTargets();
        currVerticies = new List<Vector3>();

    }
    private void LineToRobotTargets()
    {
    
    
    /*
    robotPath.transform.parent = EmptyObj.gameObject.transform;
    robotPath.
    */
    }
}