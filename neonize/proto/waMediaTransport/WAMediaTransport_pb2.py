# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: waMediaTransport/WAMediaTransport.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from waCommon import WACommon_pb2 as waCommon_dot_WACommon__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'waMediaTransport/WAMediaTransport.proto\x12\x10WAMediaTransport\x1a\x17waCommon/WACommon.proto\"\xb3\x06\n\x10WAMediaTransport\x12=\n\x08integral\x18\x01 \x01(\x0b\x32+.WAMediaTransport.WAMediaTransport.Integral\x12?\n\tancillary\x18\x02 \x01(\x0b\x32,.WAMediaTransport.WAMediaTransport.Ancillary\x1a\xa6\x04\n\tAncillary\x12\x12\n\nfileLength\x18\x01 \x01(\x04\x12\x10\n\x08mimetype\x18\x02 \x01(\t\x12I\n\tthumbnail\x18\x03 \x01(\x0b\x32\x36.WAMediaTransport.WAMediaTransport.Ancillary.Thumbnail\x12\x10\n\x08objectID\x18\x04 \x01(\t\x1a\x95\x03\n\tThumbnail\x12\x15\n\rJPEGThumbnail\x18\x01 \x01(\x0c\x12k\n\x15\x64ownloadableThumbnail\x18\x02 \x01(\x0b\x32L.WAMediaTransport.WAMediaTransport.Ancillary.Thumbnail.DownloadableThumbnail\x12\x16\n\x0ethumbnailWidth\x18\x03 \x01(\r\x12\x17\n\x0fthumbnailHeight\x18\x04 \x01(\r\x1a\xd2\x01\n\x15\x44ownloadableThumbnail\x12\x12\n\nfileSHA256\x18\x01 \x01(\x0c\x12\x15\n\rfileEncSHA256\x18\x02 \x01(\x0c\x12\x12\n\ndirectPath\x18\x03 \x01(\t\x12\x10\n\x08mediaKey\x18\x04 \x01(\x0c\x12\x19\n\x11mediaKeyTimestamp\x18\x05 \x01(\x03\x12\x10\n\x08objectID\x18\x06 \x01(\t\x12\x1d\n\x15thumbnailScansSidecar\x18\x07 \x01(\x0c\x12\x1c\n\x14thumbnailScanLengths\x18\x08 \x03(\r\x1av\n\x08Integral\x12\x12\n\nfileSHA256\x18\x01 \x01(\x0c\x12\x10\n\x08mediaKey\x18\x02 \x01(\x0c\x12\x15\n\rfileEncSHA256\x18\x03 \x01(\x0c\x12\x12\n\ndirectPath\x18\x04 \x01(\t\x12\x19\n\x11mediaKeyTimestamp\x18\x05 \x01(\x03\"\xf5\x03\n\x0eImageTransport\x12;\n\x08integral\x18\x01 \x01(\x0b\x32).WAMediaTransport.ImageTransport.Integral\x12=\n\tancillary\x18\x02 \x01(\x0b\x32*.WAMediaTransport.ImageTransport.Ancillary\x1a\xa3\x02\n\tAncillary\x12\x0e\n\x06height\x18\x01 \x01(\r\x12\r\n\x05width\x18\x02 \x01(\r\x12\x14\n\x0cscansSidecar\x18\x03 \x01(\x0c\x12\x13\n\x0bscanLengths\x18\x04 \x03(\r\x12\x1c\n\x14midQualityFileSHA256\x18\x05 \x01(\x0c\x12\x41\n\x06hdType\x18\x06 \x01(\x0e\x32\x31.WAMediaTransport.ImageTransport.Ancillary.HdType\x12!\n\x15memoriesConceptScores\x18\x07 \x03(\x02\x42\x02\x10\x01\x12\x1e\n\x12memoriesConceptIDs\x18\x08 \x03(\rB\x02\x10\x01\"(\n\x06HdType\x12\x08\n\x04NONE\x10\x00\x12\t\n\x05LQ_4K\x10\x01\x12\t\n\x05HQ_4K\x10\x02\x1a\x41\n\x08Integral\x12\x35\n\ttransport\x18\x01 \x01(\x0b\x32\".WAMediaTransport.WAMediaTransport\"\xda\x03\n\x0eVideoTransport\x12;\n\x08integral\x18\x01 \x01(\x0b\x32).WAMediaTransport.VideoTransport.Integral\x12=\n\tancillary\x18\x02 \x01(\x0b\x32*.WAMediaTransport.VideoTransport.Ancillary\x1a\x88\x02\n\tAncillary\x12\x0f\n\x07seconds\x18\x01 \x01(\r\x12&\n\x07\x63\x61ption\x18\x02 \x01(\x0b\x32\x15.WACommon.MessageText\x12\x13\n\x0bgifPlayback\x18\x03 \x01(\x08\x12\x0e\n\x06height\x18\x04 \x01(\r\x12\r\n\x05width\x18\x05 \x01(\r\x12\x0f\n\x07sidecar\x18\x06 \x01(\x0c\x12N\n\x0egifAttribution\x18\x07 \x01(\x0e\x32\x36.WAMediaTransport.VideoTransport.Ancillary.Attribution\"-\n\x0b\x41ttribution\x12\x08\n\x04NONE\x10\x00\x12\t\n\x05GIPHY\x10\x01\x12\t\n\x05TENOR\x10\x02\x1a\x41\n\x08Integral\x12\x35\n\ttransport\x18\x01 \x01(\x0b\x32\".WAMediaTransport.WAMediaTransport\"\x93\x07\n\x0e\x41udioTransport\x12;\n\x08integral\x18\x01 \x01(\x0b\x32).WAMediaTransport.AudioTransport.Integral\x12=\n\tancillary\x18\x02 \x01(\x0b\x32*.WAMediaTransport.AudioTransport.Ancillary\x1a\xce\x04\n\tAncillary\x12\x0f\n\x07seconds\x18\x01 \x01(\r\x12K\n\x0b\x61vatarAudio\x18\x02 \x01(\x0b\x32\x36.WAMediaTransport.AudioTransport.Ancillary.AvatarAudio\x1a\xe2\x03\n\x0b\x41vatarAudio\x12\x0e\n\x06poseID\x18\x01 \x01(\r\x12m\n\x10\x61vatarAnimations\x18\x02 \x03(\x0b\x32S.WAMediaTransport.AudioTransport.Ancillary.AvatarAudio.DownloadableAvatarAnimations\x1a\xfb\x01\n\x1c\x44ownloadableAvatarAnimations\x12\x12\n\nfileSHA256\x18\x01 \x01(\x0c\x12\x15\n\rfileEncSHA256\x18\x02 \x01(\x0c\x12\x12\n\ndirectPath\x18\x03 \x01(\t\x12\x10\n\x08mediaKey\x18\x04 \x01(\x0c\x12\x19\n\x11mediaKeyTimestamp\x18\x05 \x01(\x03\x12\x10\n\x08objectID\x18\x06 \x01(\t\x12]\n\x0e\x61nimationsType\x18\x07 \x01(\x0e\x32\x45.WAMediaTransport.AudioTransport.Ancillary.AvatarAudio.AnimationsType\"V\n\x0e\x41nimationsType\x12\r\n\tTALKING_A\x10\x00\x12\n\n\x06IDLE_A\x10\x01\x12\r\n\tTALKING_B\x10\x02\x12\n\n\x06IDLE_B\x10\x03\x12\x0e\n\nBACKGROUND\x10\x04\x1a\xb3\x01\n\x08Integral\x12\x35\n\ttransport\x18\x01 \x01(\x0b\x32\".WAMediaTransport.WAMediaTransport\x12J\n\x0b\x61udioFormat\x18\x02 \x01(\x0e\x32\x35.WAMediaTransport.AudioTransport.Integral.AudioFormat\"$\n\x0b\x41udioFormat\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04OPUS\x10\x01\"\xf8\x01\n\x11\x44ocumentTransport\x12>\n\x08integral\x18\x01 \x01(\x0b\x32,.WAMediaTransport.DocumentTransport.Integral\x12@\n\tancillary\x18\x02 \x01(\x0b\x32-.WAMediaTransport.DocumentTransport.Ancillary\x1a\x1e\n\tAncillary\x12\x11\n\tpageCount\x18\x01 \x01(\r\x1a\x41\n\x08Integral\x12\x35\n\ttransport\x18\x01 \x01(\x0b\x32\".WAMediaTransport.WAMediaTransport\"\xd8\x03\n\x10StickerTransport\x12=\n\x08integral\x18\x01 \x01(\x0b\x32+.WAMediaTransport.StickerTransport.Integral\x12?\n\tancillary\x18\x02 \x01(\x0b\x32,.WAMediaTransport.StickerTransport.Ancillary\x1a\xd3\x01\n\tAncillary\x12\x11\n\tpageCount\x18\x01 \x01(\r\x12\x0e\n\x06height\x18\x02 \x01(\r\x12\r\n\x05width\x18\x03 \x01(\r\x12\x18\n\x10\x66irstFrameLength\x18\x04 \x01(\r\x12\x19\n\x11\x66irstFrameSidecar\x18\x05 \x01(\x0c\x12\x14\n\x0cmustacheText\x18\x06 \x01(\t\x12\x14\n\x0cisThirdParty\x18\x07 \x01(\x08\x12\x17\n\x0freceiverFetchID\x18\x08 \x01(\t\x12\x1a\n\x12\x61\x63\x63\x65ssibilityLabel\x18\t \x01(\t\x1an\n\x08Integral\x12\x35\n\ttransport\x18\x01 \x01(\x0b\x32\".WAMediaTransport.WAMediaTransport\x12\x12\n\nisAnimated\x18\x02 \x01(\x08\x12\x17\n\x0freceiverFetchID\x18\x03 \x01(\t\"\x9d\x02\n\x10\x43ontactTransport\x12=\n\x08integral\x18\x01 \x01(\x0b\x32+.WAMediaTransport.ContactTransport.Integral\x12?\n\tancillary\x18\x02 \x01(\x0b\x32,.WAMediaTransport.ContactTransport.Ancillary\x1a \n\tAncillary\x12\x13\n\x0b\x64isplayName\x18\x01 \x01(\t\x1ag\n\x08Integral\x12\x0f\n\x05vcard\x18\x01 \x01(\tH\x00\x12?\n\x11\x64ownloadableVcard\x18\x02 \x01(\x0b\x32\".WAMediaTransport.WAMediaTransportH\x00\x42\t\n\x07\x63ontactB,Z*go.mau.fi/whatsmeow/proto/waMediaTransport')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'waMediaTransport.WAMediaTransport_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z*go.mau.fi/whatsmeow/proto/waMediaTransport'
  _IMAGETRANSPORT_ANCILLARY.fields_by_name['memoriesConceptScores']._options = None
  _IMAGETRANSPORT_ANCILLARY.fields_by_name['memoriesConceptScores']._serialized_options = b'\020\001'
  _IMAGETRANSPORT_ANCILLARY.fields_by_name['memoriesConceptIDs']._options = None
  _IMAGETRANSPORT_ANCILLARY.fields_by_name['memoriesConceptIDs']._serialized_options = b'\020\001'
  _globals['_WAMEDIATRANSPORT']._serialized_start=87
  _globals['_WAMEDIATRANSPORT']._serialized_end=906
  _globals['_WAMEDIATRANSPORT_ANCILLARY']._serialized_start=236
  _globals['_WAMEDIATRANSPORT_ANCILLARY']._serialized_end=786
  _globals['_WAMEDIATRANSPORT_ANCILLARY_THUMBNAIL']._serialized_start=381
  _globals['_WAMEDIATRANSPORT_ANCILLARY_THUMBNAIL']._serialized_end=786
  _globals['_WAMEDIATRANSPORT_ANCILLARY_THUMBNAIL_DOWNLOADABLETHUMBNAIL']._serialized_start=576
  _globals['_WAMEDIATRANSPORT_ANCILLARY_THUMBNAIL_DOWNLOADABLETHUMBNAIL']._serialized_end=786
  _globals['_WAMEDIATRANSPORT_INTEGRAL']._serialized_start=788
  _globals['_WAMEDIATRANSPORT_INTEGRAL']._serialized_end=906
  _globals['_IMAGETRANSPORT']._serialized_start=909
  _globals['_IMAGETRANSPORT']._serialized_end=1410
  _globals['_IMAGETRANSPORT_ANCILLARY']._serialized_start=1052
  _globals['_IMAGETRANSPORT_ANCILLARY']._serialized_end=1343
  _globals['_IMAGETRANSPORT_ANCILLARY_HDTYPE']._serialized_start=1303
  _globals['_IMAGETRANSPORT_ANCILLARY_HDTYPE']._serialized_end=1343
  _globals['_IMAGETRANSPORT_INTEGRAL']._serialized_start=1345
  _globals['_IMAGETRANSPORT_INTEGRAL']._serialized_end=1410
  _globals['_VIDEOTRANSPORT']._serialized_start=1413
  _globals['_VIDEOTRANSPORT']._serialized_end=1887
  _globals['_VIDEOTRANSPORT_ANCILLARY']._serialized_start=1556
  _globals['_VIDEOTRANSPORT_ANCILLARY']._serialized_end=1820
  _globals['_VIDEOTRANSPORT_ANCILLARY_ATTRIBUTION']._serialized_start=1775
  _globals['_VIDEOTRANSPORT_ANCILLARY_ATTRIBUTION']._serialized_end=1820
  _globals['_VIDEOTRANSPORT_INTEGRAL']._serialized_start=1345
  _globals['_VIDEOTRANSPORT_INTEGRAL']._serialized_end=1410
  _globals['_AUDIOTRANSPORT']._serialized_start=1890
  _globals['_AUDIOTRANSPORT']._serialized_end=2805
  _globals['_AUDIOTRANSPORT_ANCILLARY']._serialized_start=2033
  _globals['_AUDIOTRANSPORT_ANCILLARY']._serialized_end=2623
  _globals['_AUDIOTRANSPORT_ANCILLARY_AVATARAUDIO']._serialized_start=2141
  _globals['_AUDIOTRANSPORT_ANCILLARY_AVATARAUDIO']._serialized_end=2623
  _globals['_AUDIOTRANSPORT_ANCILLARY_AVATARAUDIO_DOWNLOADABLEAVATARANIMATIONS']._serialized_start=2284
  _globals['_AUDIOTRANSPORT_ANCILLARY_AVATARAUDIO_DOWNLOADABLEAVATARANIMATIONS']._serialized_end=2535
  _globals['_AUDIOTRANSPORT_ANCILLARY_AVATARAUDIO_ANIMATIONSTYPE']._serialized_start=2537
  _globals['_AUDIOTRANSPORT_ANCILLARY_AVATARAUDIO_ANIMATIONSTYPE']._serialized_end=2623
  _globals['_AUDIOTRANSPORT_INTEGRAL']._serialized_start=2626
  _globals['_AUDIOTRANSPORT_INTEGRAL']._serialized_end=2805
  _globals['_AUDIOTRANSPORT_INTEGRAL_AUDIOFORMAT']._serialized_start=2769
  _globals['_AUDIOTRANSPORT_INTEGRAL_AUDIOFORMAT']._serialized_end=2805
  _globals['_DOCUMENTTRANSPORT']._serialized_start=2808
  _globals['_DOCUMENTTRANSPORT']._serialized_end=3056
  _globals['_DOCUMENTTRANSPORT_ANCILLARY']._serialized_start=2959
  _globals['_DOCUMENTTRANSPORT_ANCILLARY']._serialized_end=2989
  _globals['_DOCUMENTTRANSPORT_INTEGRAL']._serialized_start=1345
  _globals['_DOCUMENTTRANSPORT_INTEGRAL']._serialized_end=1410
  _globals['_STICKERTRANSPORT']._serialized_start=3059
  _globals['_STICKERTRANSPORT']._serialized_end=3531
  _globals['_STICKERTRANSPORT_ANCILLARY']._serialized_start=3208
  _globals['_STICKERTRANSPORT_ANCILLARY']._serialized_end=3419
  _globals['_STICKERTRANSPORT_INTEGRAL']._serialized_start=3421
  _globals['_STICKERTRANSPORT_INTEGRAL']._serialized_end=3531
  _globals['_CONTACTTRANSPORT']._serialized_start=3534
  _globals['_CONTACTTRANSPORT']._serialized_end=3819
  _globals['_CONTACTTRANSPORT_ANCILLARY']._serialized_start=3682
  _globals['_CONTACTTRANSPORT_ANCILLARY']._serialized_end=3714
  _globals['_CONTACTTRANSPORT_INTEGRAL']._serialized_start=3716
  _globals['_CONTACTTRANSPORT_INTEGRAL']._serialized_end=3819
# @@protoc_insertion_point(module_scope)
