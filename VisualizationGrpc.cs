// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: visualization.proto
// </auto-generated>
#pragma warning disable 0414, 1591
#region Designer generated code

using grpc = global::Grpc.Core;

namespace Visualization {
  public static partial class Visualization
  {
    static readonly string __ServiceName = "visualization.Visualization";

    static readonly grpc::Marshaller<global::Visualization.MarkerRequest> __Marshaller_visualization_MarkerRequest = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Visualization.MarkerRequest.Parser.ParseFrom);
    static readonly grpc::Marshaller<global::Visualization.Marker> __Marshaller_visualization_Marker = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Visualization.Marker.Parser.ParseFrom);
    static readonly grpc::Marshaller<global::Visualization.MarkerArray> __Marshaller_visualization_MarkerArray = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Visualization.MarkerArray.Parser.ParseFrom);

    static readonly grpc::Method<global::Visualization.MarkerRequest, global::Visualization.Marker> __Method_SetMarker = new grpc::Method<global::Visualization.MarkerRequest, global::Visualization.Marker>(
        grpc::MethodType.ServerStreaming,
        __ServiceName,
        "SetMarker",
        __Marshaller_visualization_MarkerRequest,
        __Marshaller_visualization_Marker);

    static readonly grpc::Method<global::Visualization.MarkerRequest, global::Visualization.MarkerArray> __Method_SetMarkerArray = new grpc::Method<global::Visualization.MarkerRequest, global::Visualization.MarkerArray>(
        grpc::MethodType.ServerStreaming,
        __ServiceName,
        "SetMarkerArray",
        __Marshaller_visualization_MarkerRequest,
        __Marshaller_visualization_MarkerArray);

    /// <summary>Service descriptor</summary>
    public static global::Google.Protobuf.Reflection.ServiceDescriptor Descriptor
    {
      get { return global::Visualization.VisualizationReflection.Descriptor.Services[0]; }
    }

    /// <summary>Base class for server-side implementations of Visualization</summary>
    [grpc::BindServiceMethod(typeof(Visualization), "BindService")]
    public abstract partial class VisualizationBase
    {
      public virtual global::System.Threading.Tasks.Task SetMarker(global::Visualization.MarkerRequest request, grpc::IServerStreamWriter<global::Visualization.Marker> responseStream, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      public virtual global::System.Threading.Tasks.Task SetMarkerArray(global::Visualization.MarkerRequest request, grpc::IServerStreamWriter<global::Visualization.MarkerArray> responseStream, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

    }

    /// <summary>Client for Visualization</summary>
    public partial class VisualizationClient : grpc::ClientBase<VisualizationClient>
    {
      /// <summary>Creates a new client for Visualization</summary>
      /// <param name="channel">The channel to use to make remote calls.</param>
      public VisualizationClient(grpc::ChannelBase channel) : base(channel)
      {
      }
      /// <summary>Creates a new client for Visualization that uses a custom <c>CallInvoker</c>.</summary>
      /// <param name="callInvoker">The callInvoker to use to make remote calls.</param>
      public VisualizationClient(grpc::CallInvoker callInvoker) : base(callInvoker)
      {
      }
      /// <summary>Protected parameterless constructor to allow creation of test doubles.</summary>
      protected VisualizationClient() : base()
      {
      }
      /// <summary>Protected constructor to allow creation of configured clients.</summary>
      /// <param name="configuration">The client configuration.</param>
      protected VisualizationClient(ClientBaseConfiguration configuration) : base(configuration)
      {
      }

      public virtual grpc::AsyncServerStreamingCall<global::Visualization.Marker> SetMarker(global::Visualization.MarkerRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return SetMarker(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual grpc::AsyncServerStreamingCall<global::Visualization.Marker> SetMarker(global::Visualization.MarkerRequest request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncServerStreamingCall(__Method_SetMarker, null, options, request);
      }
      public virtual grpc::AsyncServerStreamingCall<global::Visualization.MarkerArray> SetMarkerArray(global::Visualization.MarkerRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return SetMarkerArray(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual grpc::AsyncServerStreamingCall<global::Visualization.MarkerArray> SetMarkerArray(global::Visualization.MarkerRequest request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncServerStreamingCall(__Method_SetMarkerArray, null, options, request);
      }
      /// <summary>Creates a new instance of client from given <c>ClientBaseConfiguration</c>.</summary>
      protected override VisualizationClient NewInstance(ClientBaseConfiguration configuration)
      {
        return new VisualizationClient(configuration);
      }
    }

    /// <summary>Creates service definition that can be registered with a server</summary>
    /// <param name="serviceImpl">An object implementing the server-side handling logic.</param>
    public static grpc::ServerServiceDefinition BindService(VisualizationBase serviceImpl)
    {
      return grpc::ServerServiceDefinition.CreateBuilder()
          .AddMethod(__Method_SetMarker, serviceImpl.SetMarker)
          .AddMethod(__Method_SetMarkerArray, serviceImpl.SetMarkerArray).Build();
    }

    /// <summary>Register service method with a service binder with or without implementation. Useful when customizing the  service binding logic.
    /// Note: this method is part of an experimental API that can change or be removed without any prior notice.</summary>
    /// <param name="serviceBinder">Service methods will be bound by calling <c>AddMethod</c> on this object.</param>
    /// <param name="serviceImpl">An object implementing the server-side handling logic.</param>
    public static void BindService(grpc::ServiceBinderBase serviceBinder, VisualizationBase serviceImpl)
    {
      serviceBinder.AddMethod(__Method_SetMarker, serviceImpl == null ? null : new grpc::ServerStreamingServerMethod<global::Visualization.MarkerRequest, global::Visualization.Marker>(serviceImpl.SetMarker));
      serviceBinder.AddMethod(__Method_SetMarkerArray, serviceImpl == null ? null : new grpc::ServerStreamingServerMethod<global::Visualization.MarkerRequest, global::Visualization.MarkerArray>(serviceImpl.SetMarkerArray));
    }

  }
}
#endregion
