// Upgrade NOTE: replaced '_Object2World' with 'unity_ObjectToWorld'

Shader "Custom/SnowTrailShaderGeometry"
{
	Properties
	{
		_Color ("Main Color", Color) = (.5,.5,.5,1)
		_Offset ("Z Buffer Offset", Float) = 0.02
	}
	SubShader
	{
		Tags { "RenderType"="Opaque" "Queue" = "Geometry-75" }
		Offset -1, -1
		ZWrite Off
		
		CGPROGRAM
		#pragma surface surf Lambert vertex:vert

		#include "UnityCG.cginc"

		float4 _Color;
		
		void vert(inout appdata_full v)
		{
			float3 viewDir = WorldSpaceViewDir(v.vertex);
			float viewDirLength = length(viewDir);
			v.vertex.xyz += normalize(viewDir)*min(viewDirLength*0.75, 0.75);
		}

		struct Input
		{
			float noEmptyStruct;
		};

		void surf (Input IN, inout SurfaceOutput o)
		{
			o.Albedo = _Color.rgb;
			o.Alpha = _Color.a;
		}
		ENDCG
		
		Pass
        {
			Name "ZWriter"
			Blend One One
			Offset -1, -1
			ZWrite On
			
			CGPROGRAM
			#pragma vertex vert
			#pragma fragment frag
			#pragma fragmentoption ARB_precision_hint_fastest
			#include "UnityCG.cginc"
			
			struct v2f
			{
				float4 pos          : POSITION;
			};
			
			float _Offset;
			
			v2f vert (appdata_full v)
			{
				v2f o;
				
				o.pos = mul(unity_ObjectToWorld, v.vertex);
				
				// apply z buffer offset
				float3 zOffset = _Offset*normalize(_WorldSpaceCameraPos - o.pos.xyz);
				o.pos.xyz += zOffset;
				
				o.pos = mul(UNITY_MATRIX_VP, o.pos);
				
				//o.pos = mul(UNITY_MATRIX_MVP, v.vertex + _Offset*normalize(mul(_World2Object, float4(_WorldSpaceCameraPos, 1)) - v.vertex));
				return o;
			}
			
			half4 frag(v2f i) : COLOR
			{
				return half4(0, 0, 0, 0);
			}
			ENDCG
        }
	}
}
