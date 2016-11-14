// Code generated by Wire protocol buffer compiler, do not edit.
// Source file: business/diary.proto at 19:1
package me.littlekey.duoyu.model.proto;

import com.squareup.wire.FieldEncoding;
import com.squareup.wire.Message;
import com.squareup.wire.ProtoAdapter;
import com.squareup.wire.ProtoReader;
import com.squareup.wire.ProtoWriter;
import com.squareup.wire.WireField;
import com.squareup.wire.internal.Internal;
import java.io.IOException;
import java.lang.Object;
import java.lang.Override;
import java.lang.String;
import java.lang.StringBuilder;
import okio.ByteString;

public final class RecentRequest extends Message<RecentRequest, RecentRequest.Builder> {
  public static final ProtoAdapter<RecentRequest> ADAPTER = new ProtoAdapter_RecentRequest();

  private static final long serialVersionUID = 0L;

  @WireField(
      tag = 1,
      adapter = "me.littlekey.duoyu.model.proto.Cursor#ADAPTER"
  )
  public final Cursor cursor;

  public RecentRequest(Cursor cursor) {
    this(cursor, ByteString.EMPTY);
  }

  public RecentRequest(Cursor cursor, ByteString unknownFields) {
    super(ADAPTER, unknownFields);
    this.cursor = cursor;
  }

  @Override
  public Builder newBuilder() {
    Builder builder = new Builder();
    builder.cursor = cursor;
    builder.addUnknownFields(unknownFields());
    return builder;
  }

  @Override
  public boolean equals(Object other) {
    if (other == this) return true;
    if (!(other instanceof RecentRequest)) return false;
    RecentRequest o = (RecentRequest) other;
    return unknownFields().equals(o.unknownFields())
        && Internal.equals(cursor, o.cursor);
  }

  @Override
  public int hashCode() {
    int result = super.hashCode;
    if (result == 0) {
      result = unknownFields().hashCode();
      result = result * 37 + (cursor != null ? cursor.hashCode() : 0);
      super.hashCode = result;
    }
    return result;
  }

  @Override
  public String toString() {
    StringBuilder builder = new StringBuilder();
    if (cursor != null) builder.append(", cursor=").append(cursor);
    return builder.replace(0, 2, "RecentRequest{").append('}').toString();
  }

  public static final class Builder extends Message.Builder<RecentRequest, Builder> {
    public Cursor cursor;

    public Builder() {
    }

    public Builder cursor(Cursor cursor) {
      this.cursor = cursor;
      return this;
    }

    @Override
    public RecentRequest build() {
      return new RecentRequest(cursor, super.buildUnknownFields());
    }
  }

  private static final class ProtoAdapter_RecentRequest extends ProtoAdapter<RecentRequest> {
    ProtoAdapter_RecentRequest() {
      super(FieldEncoding.LENGTH_DELIMITED, RecentRequest.class);
    }

    @Override
    public int encodedSize(RecentRequest value) {
      return (value.cursor != null ? Cursor.ADAPTER.encodedSizeWithTag(1, value.cursor) : 0)
          + value.unknownFields().size();
    }

    @Override
    public void encode(ProtoWriter writer, RecentRequest value) throws IOException {
      if (value.cursor != null) Cursor.ADAPTER.encodeWithTag(writer, 1, value.cursor);
      writer.writeBytes(value.unknownFields());
    }

    @Override
    public RecentRequest decode(ProtoReader reader) throws IOException {
      Builder builder = new Builder();
      long token = reader.beginMessage();
      for (int tag; (tag = reader.nextTag()) != -1;) {
        switch (tag) {
          case 1: builder.cursor(Cursor.ADAPTER.decode(reader)); break;
          default: {
            FieldEncoding fieldEncoding = reader.peekFieldEncoding();
            Object value = fieldEncoding.rawProtoAdapter().decode(reader);
            builder.addUnknownField(tag, fieldEncoding, value);
          }
        }
      }
      reader.endMessage(token);
      return builder.build();
    }

    @Override
    public RecentRequest redact(RecentRequest value) {
      Builder builder = value.newBuilder();
      if (builder.cursor != null) builder.cursor = Cursor.ADAPTER.redact(builder.cursor);
      builder.clearUnknownFields();
      return builder.build();
    }
  }
}